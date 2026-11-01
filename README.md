# Kichi-Kichi

カメラでテーブルの上を認識し、**片付け**と**拭き上げ**を自動で行う掃除ロボット。台車が付いており、テーブル間を移動する。

> A cleaning robot that sees the table with a camera and automatically **clears** it and **wipes** it down.


## 概要 / Overview

TabulaSense は、施設内を移動し、テーブルの上にある「片付けるべき物」と「拭き取るべき汚れ」をカメラで見分け、
アームで物を回収したあと、ワイパー／モップでテーブル表面を自動で拭き上げるロボットです。
また下げ膳なども行います。スタッフのやり方を見て真似し、言われたことを覚えていく自己学習機能を備えています。


- 「エプロンの人」「今話した人」のように言葉で相手を決めて確認し、「ついてきて」と言われたらスタッフの後ろをついて動きます。移動しながら、壁やテーブルの形を地図に描きつつ自分の位置を把握し、同時に「丸いテーブル」のような目印を地図メモリに書き込みます。スタッフが「ここが3番テーブルね」と教えると、LLMが名前を取り出し、今いる場所に一番近い目印に結び付けます。自動の名前と人が教えた名前が食い違った場合は、人が教えた名前を優先します。

- 「窓際のテーブルを拭いて」と言われると、LLMが指示を「動作は拭く、種類はテーブル、窓の近く」に分解します。

- 場所：地図メモリから条件に合う目印を探します。一つなら決定、複数なら「どちらのテーブルですか？」、一つもなければ「案内してもらえますか？」と聞き返します。この時、動作と対象をもとにルール記憶を検索し、該当するものを計画の条件に加えます。例えば「拭く前に物があれば片付ける」「端まで拭く」です。

- 動作辞書を言い換えも含めて引きます。「拭く」がなければ「一度やって見せてもらえますか？」と頼み、スタッフが拭く様子を撮影します。その動画を見本として動作辞書に登録し、見本をもとに動作を実行できるようにします。手順が複数ある場合（物を片付けてから拭く、など）は、LLMが「つかむ→置く/捨てる→拭く」のように部品動作に分け、足りない部品だけ見せてもらいます。

- 片付け：テーブルに物があれば、ルール記憶で置き場所を探します。わからなければ物を持ってスタッフのところへ戻り、「これはどこに置けばいいですか？」と聞いて、答えを置き場所ルールとして保存します。ゴミ箱のフタが閉じていれば、フタを開ける動作を呼び出します。また腕が届く範囲には限りがあるので、ルールで決まった範囲（例：縁まで）をカバーできる立ち位置を複数決め、その位置を順に回ります。各位置では、動作辞書に登録された実行モデルでゆっくり拭きます。

- カメラで拭き残しを確認し、残っていればその部分をやり直します。確認の基準にはルールも使います。例えば「端まで」のルールがあれば、縁の部分も重点的にチェックします。

- スタッフの指摘は内容で行き先が分かれます。このとき、スポンジや手の3D軌道を追い、ロボットの手先の目標にします。腕の関節の動きはロボット側で計算（逆運動学）し、届かない部分は台車の位置で補います

- 動きのずれ（「もう少し強く押して」）ではその区間を介入データとして実行記録に残します。この時、意味・手順の指摘（「端まで拭いて」「物があったら捨てて」）：理由ごとルール記憶に保存し、次回の計画から即座に反映します。適用範囲が曖昧なら、その場で「全部のテーブルでそうしますか？」と確認します。既存のルールと食い違う場合は、「前は○○と教わりましたが、変えますか？」と確認してから上書きします。



## 開発目標（MVP） / Development goals (MVP)

XLeRobotをMuJoCoでシミュレーションし、最新論文を実装して精度向上も目指す。
さらに、XLeRobot（自費で購入し組み立て、初期は計算はクラウドで行い、自宅で作動するかテストする。
例えば部屋を案内し、「テーブルを掃除して」という抽象的な命令も実行できるようにする。
そして顧客で試験導入しながら精度向上を目指す。
YORのシミュレーションモデルを作成し、YOR(https://yourownrobot.ai/)を助成金で購入しさらにPoCを行う。YORのソフトはアップデートのたびにクラウドを通して遠隔で更新されるようにする。



### Step 0：開発環境の準備
> 構築手順は [docs/setup.md](docs/setup.md)（`bash scripts/setup.sh` で自動構築）

このプロジェクトではUbuntu の中（/home/expo7/Kichi-Kichi）に必要な編集ファイルを用意します。

### Step 1：シミュレーション上にロボットを構築
- XLeRobotのモデルをMuJoCoに読み込む

まずファイルのパスを扱うための機能を読み込みます
```python
from pathlib import Path
```
次にMuJoCo本体とロボットを3D表示するビューアを読み込みます。
```python
import mujoco
import mujoco.viewer
```
次に、このフォルダにはscene.xmlというMuJoCo に「何を、どんな環境・物理条件で表示してシミュレーションするか」を伝える XML 形式の設定ファイルがあります。
そこでMuJoCoはモデルを読み込むときにscene.xml がどこにあるかを知る必要があります。
まず以下のように右側で作った scene.xml のパスを、model_path という名前で使えるようにします。
```python
model_path = 結果
```
ここでもし以下のように書くと、問題が発生します。
```python
model_path = Path("scene.xml")
```
これだと、Python は「ターミナルで今いるフォルダにある scene.xml」を探します。別のフォルダからスクリプトを実行すると、見つからないことがあります。
今回の目的は、/home/expo7/Kichi-Kichi/sim/xlerobot/scene.xmlというパスを指定することです。ここで以下のコードを書きます。
```python
model_path = Path(__file__).resolve().with_name("scene.xml")
```
Path(__file__).resolve()のうち、__file__ は実行中の .py ファイルのパスです。Path(__file__) は、そのパスを Path 形式にします。
.resolve() は、相対パスなら絶対パスに変換し、パスを整理します。このあと、.with_name("scene.xml") をつなげると、ファイル名を置き換えて scene.xml のパスを作れます。

この次にこのXMLファイルを読み込み、MuJoCoのモデルを作ってmodelという変数に代入します。
まずMuJoCoの関数にファイルパスとして渡すためにパスをstr(model_path)で文字列に変換します。
次にこのXMLを読み込んでmujoco.MjModel.from_xml_pathでロボットや床、関節などのモデル定義を作ります。
```python
model = mujoco.MjModel.from_xml_path(str(model_path))
```
これでmodelはロボットの構造や設定を表しますが、次は関節の位置や速度など、シミュレーションで変わっていく値を入れていきます。
```python
data = mujoco.MjData(model)
```
 mujoco.MjDataはシミュレーション中に変化する状態を扱うクラスになります。
次にモデルを表示するビューアを起動します。with を使うことで、ブロックを抜けたときにビューアが適切に終了します。
```python
with mujoco.viewer.launch_passive(model, data) as viewer:
```
最後にビューアが開いている間、シミュレーションを1ステップ進めます。ステップごとにロボットの状態が更新されます。最後にシミュレーションの状態をビューアの表示に反映します。
```python
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
```        
これを起動すると以下のようになります。
<img width="1365" height="693" alt="スクリーンショット 2026-10-31 163151" src="https://github.com/user-attachments/assets/59a77b46-42ca-446d-a1da-739f2a409af9" />

今回はシミュレーション環境にUnityを活用したいと思います。

### Step 2：追従機能の構築
- 「エプロンの人」「今話した人」のように言葉で相手を決めて確認し、「ついてきて」と言われたらスタッフの後ろをついて動きながら、壁やテーブルの形を地図に描きつつ自分の位置を把握し、同時に「丸いテーブル」のような目印を地図メモリに書き込む仕組みを実装していきます。

まずこれではカメラ映像から地図を作れることを目標にしていきたいと思います。これは実機に移植した際に、センサー類などを極力最小限にして実装したいためです。
最初に台車の上部に固定する前向きのRGB-Dカメラ1台をシミュレーションで実装します。RGB-DカメラはRGB画像と深度情報を出力します。

最初にMuJoCoのモデルに台車固定のカメラを一つ定義します。xlerobot.xml の<body name="chassis"> の中に、カメラ要素を追加します。

```python
      <camera name="main_camera" pos="-0.35 0 0.95" xyaxes="0 -1 0 0.34 0 0.94" fovy="70"/>
```
これで pos="0.5 0.5 0.5は親ボディからの位置で順にX,Y,Z座標で単位はメートルです。euler="-30 0 45"はX,Y,Z軸まわりの回転角です。そしてfovy="45"でカメラの縦方向の視野角となります。
次にカメラ画像を一枚取得して位置と向きが合っているか確認します。まずこのカメラのライブ映像を見るために、MuJoCoビューアの視点をmain_cameraに切り替えます。
これからロボット全体の映像とカメラ映像のウィンドウを同時に表示します。

まず以下のようにMuJoCoでカメラ画像を描写するための準備をします。
```python
renderer = mujoco.Renderer(model, height=480, width=640)
```
これでmujoco.Rendererで画像を生成するレンダラーを作成します。
```python
with mujoco.viewer.launch_passive(model,data)as viewer:
```
この行ではlaunch_passiveでビューアを開き、起動したビューアをviewerという変数で扱えるようにします。
そしてビューアが開いている間、つまりviewer.is_running():が起動している間はビューアとシミュレーション状態を共有しながらシミュレーションを１ステップずつ進めるようにします。しかしMuJoCoでは、Pythonのプログラムとビューアが、ロボットの状態（関節の角度や位置など）を共有しています。片方が状態を書き換えている途中に、もう片方が同時に読んだり書いたりすると、処理がぶつかる可能性があります。そこで以下の処理をします。
```python
with viewer.lock():
                mujoco.mj_step(model,data)
```
これで一時的にviewer.lock()で鍵をとり、  mujoco.mj_step(model,data)を実行し、ブロックを抜けると鍵を自動で返却する仕組みです。ここでwithを使うことで、処理中にエラーが起きても鍵を自動で返す仕組みになります。
次にMuJoCoのカメラ映像を１フレーム作る処理を行います。
ループのたびに実行すると、現在の状態に合わせて画像が更新されます。
```python
renderer.update_scene(data, camera="main_camera")
```
次に準備した描写内容を画像として生成し、imageに入れます。これによりPythonで扱える画像データを作ります。
```python
image_bgr = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
```
これはMuJoCoが返した画像の色の並びをOpenCV用に変換しています。なぜならOpenCVの表示にそのままRGB画像を渡すと、赤と青が入れ替わって見えることがあります。だから表示前に変換しています。
最後にカメラ映像のウィンドウで"q"キーが押されたらループを終了する処理をします。
```python
if cv2.waitKey(1)& 0xFF==ord("q"):
                break
```python
ここでcv2.waitKey(1)はOpenCVのウィンドウでキー入力を約１ミリ秒定期し、これでウィンドウの表示を更新します。
そして& 0xFFでキーコードの下位8ビットだけを取り出します。これが文字qのキーコードと同じかどうか識別します。
最後にtryブロックが終わった後に、MuJoCoの画像レンダラーを閉じ、OpenCVが開いた画像ウィンドウをすべて閉じます。
```python
finally:
    renderer.release()
    cv2.destroyAllWindows()
```
全体のコードは以下の通りです。
```python
from pathlib import Path
import time

import mujoco
import mujoco.viewer
import cv2

model_path = Path(__file__).resolve().with_name("scene.xml")

model = mujoco.MjModel.from_xml_path(str(model_path))#
data = mujoco.MjData(model)

renderer = mujoco.Renderer(model, height=480, width=640)
try:
    with mujoco.viewer.launch_passive(model,data)as viewer:
        while viewer.is_running():
            with viewer.lock():
                mujoco.mj_step(model,data)
                renderer.update_scene(data, camera="main_camera")
                image = renderer.render()
            viewer.sync()

            image_bgr = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            cv2.imshow("main_camerar",image_bgr)
            if cv2.waitKey(1)& 0xFF==ord("q"):
                break

finally:
    renderer.close()
    cv2.destroyAllWindows()


```


# Kichi-Kichi

カメラでテーブルの上を認識し、**片付け**と**拭き上げ**を自動で行う掃除ロボット。台車が付いており、テーブル間を移動する。

Kichi-Kichi は、施設内を移動し、テーブルの上にある「片付けるべき物」と「拭き取るべき汚れ」をカメラで見分け、
アームで物を回収したあと、ワイパー／モップでテーブル表面を自動で拭き上げるロボットです。
また下げ膳なども行います。スタッフのやり方を見て真似し、言われたことを覚えていく自己学習機能を備えています。

## 開発目標（MVP） / Development goals (MVP)


## 最優先でやるもの

全て英語でアウトプット

E資格 
https://ai-academy.deepsquare.deloitte.jp/courses/e-qualification/

R検定
https://robotmate-hub.com/r-certification/



## 後からやるもの

Fundamentals of Reinforcement Learning（アルバータ大学）
https://www.coursera.org/learn/fundamentals-of-reinforcement-learning

Modern AI Models for Vision and Multimodal Understanding
https://www.coursera.org/learn/modern-ai-models-vision-multimodal-understanding#credits


Modern Robotics: Mechanics, Planning, and Control Specialization（ノースウェスタン大学 / Kevin Lynch教授）
https://www.coursera.org/specializations/modernrobotics


3D Reconstruction - Multiple Viewpoints（コロンビア大学）
https://www.coursera.org/learn/3d-reconstruction-multiple-viewpoints

Humanoid workflow: Train locomotion in AGILE and deploy in Isaac Sim — Isaac Sim Documentation
https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_humanoid_workflow.html

LeRobotでの検証
https://wiki.seeedstudio.com/lerobot_so100m_new/

「熟練者の作業を遠くから撮影して解説を聞かせるだけで、人間以上に速く・無駄なく作業をこなすロボットの頭脳（AI）」を開発することです。このAIを安価な市販ロボットアームに搭載し、導入の手軽さを武器に工場・物流現場へ展開して資金調達と起業を実現します。
既存の論文の多くは「人間の動きをそのまま真似させる数式」を使っていますが、それでは人間の無駄な動きや遅さまでコピーしてしまいます。そこで、離れたカメラの映像と解説音声から「作業の空間構造」と「達成すべき目的」だけを抜き出し、ロボットの一人称視点へ座標変換する幾何学的な数式を組みます。さらに、「人間の手順をなぞるのではなく、最短距離・最小エネルギーでその目的を達成するほど高得点になる」という独自の報酬関数（目的関数）を数式として設計し、仮想空間内の強化学習でロボットに人間以上の効率的な動きを自力で発見させます。
また未知の物体に対しては触覚センサー付きの手を使い、物体を回転させて多角的に物体の形状を捉え、また力を加えて形状がどれくらい変形するかを観測することで物体の硬度を予想し、シミュレータに物体を形成しデータとして保存。また自ら動く物質に関しては、フレームごとに形状を予測しシミュレーションに合成(間違えていたらユーザーが任意に修正)し、関節や可動部を予測して動きや粘性などを予測し、動画とシミュレーションを見比べて差異があればシミュレーションの値を自ら調整し、該当の物質に近いものを合成。正しい性質ならそれで大量のシミュレーションを行い強化学習によりその物質を保存する。」

MABEL
(https://robotmabel.github.io/website/)のシミュレーションモデルを作成し、助成金で購入しさらにPoCを実施
　

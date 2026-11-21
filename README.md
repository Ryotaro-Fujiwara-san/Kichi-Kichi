# Kichi-Kichi



## 開発目標（MVP） / Development goals (MVP)

熟練者の作業を離れた場所からカメラで撮影し、解説を聞かせ、実際に作業をやってみせて修正を繰り返すことで、人間以上に速く無駄なく作業をこなせ、ロボットに新しい動きを教えられる学習エンジンを開発することが私たちの目標です。この熟練者の作業をカメラで撮って音声で説明するだけで、翌日には現場で動くノーコード立ち上げエンジン（人間による微修正UI付き）により、従来のロボットの導入コストを大幅に下げ、学習エンジンを搭載したAIを安価な市販ロボットアームに搭載し、導入の手軽さを武器に工場や物流の現場へ展開することで、資金調達と起業を実現します。
従来の多くの研究では「人間の動きをそのまま真似させる数式」が使われていましたが、この方法では人間の無駄な動きや作業の遅さまでコピーしてしまいます。そこで私たちは、離れたカメラの映像と解説音声から「作業空間の立体的な構造」と「達成すべき目的」だけを抜き出し、ロボット自身の目線（一人称視点）へと変換する幾何学的な数式を構築します。さらに、人間の手順をなぞるのではなく、「最短距離かつ最小のエネルギーで目的を達成するほど高得点になる」という独自の評価基準（報酬関数）を数式として設計します。これにより、ロボットは仮想空間での試行錯誤（強化学習）を通じて、作業の意図を理解し、人間を超える効率的な動きを自力で発見できるようになります。
また、初めて扱う未知の物体に対しても、ロボットは自律的に学習して対応します。触覚センサー付きのハンドを使って物体を回転させながら多角的に形を捉え、さらに力を加えてどれくらい変形するかを観測することで、その物体の硬さを予測します。こうして得られた形状や硬さの情報は、仮想空間（シミュレータ）内に立体データとして再現し、保存します。
データが完成したら、仮想空間で大量のシミュレーション（強化学習）を行い、その物質を自在に扱える知識として保存します。
最終的には、MABEL( https://robotmabel.github.io/website/ )のような安価な機体が特別なファインチューニング作業を通さずに、特定のタスクをこなせるように学習エンジン付きのAIを搭載します。

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

MABEL
(https://robotmabel.github.io/website/)のシミュレーションモデルを作成し、助成金で購入しさらにPoCを実施
　

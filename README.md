# Evolutionary Model Merge
[Evolutionary Optimization of Model Merging Recipes](https://sakana.ai/evolutionary-model-merge-jp/)

### Install Libraries
```
git clone https://github.com/arcee-ai/mergekit.git
cd mergekit
pip install -e .[evolve]
```

### Dataset
[MGSM](https://huggingface.co/datasets/juletxara/mgsm)

### Model Merge
```
mergekit-evolve ./evol_merge_config.yml \
		--storage-path evol_merge_storage \
		--task-search-path eval_tasks \
		--in-memory \
		--no-merge-cuda --wandb
```

### Save Best Parameter
```
mergekit-yaml evol_merge_storage/best_config.yaml merge
```

### Evaluate
```
Python test.py
```

#### Example
```
Question: 次の数学の問題を解いてください。最終的な答えを出す前に、解答の推論過程を記述してください。答えには整数の答え以外何も追加しないでください。
問題:ジャネットのアヒルは1日に16個の卵を生みます。ジャネットは毎朝朝食の一環で3個を消費し、毎日4個使って友達向けにマフィンを焼きます。残りを市場で1個あたり2ドルの価格で売ります。彼女は毎日市場でいくら手に入れていますか?
```
| Base Model(augmxnt/shisa-gamma-7b-v1) | Source(WizardLMTeam/WizardMath-7B-V1.1 ) | Merge Model |
| -- | -- | -- |
| 彼女は毎日8ドル手に入れています。 | 首尾connect. 1日16個卵生み、3個消費、4個マフィン焼き、市場で1個あたり2ドル売り、16-3-4=9個市場で売ります。 9個卵1日売るので、9*2=18ドル手に入れます。 18 The answer is: 18. | 16 - 3 - 4 = 9 9 x 2 = 18 The answer is: 18. |

### Citation
- https://acro-engineer.hatenablog.com/entry/2024/05/07/124507
- https://note.com/npaka/n/n42129c043026
- https://github.com/openai/simple-evals/tree/main

### TODO
#### Trainデータ(8件)
- 2値スコア(acc:0のまま進めるとどうなるかを確認)

#### Train+Testデータ
- 2値スコア
- Trainの8件のみanswerを使う
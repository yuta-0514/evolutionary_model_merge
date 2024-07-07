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
### Citation
- https://acro-engineer.hatenablog.com/entry/2024/05/07/124507
- https://note.com/npaka/n/n42129c043026
- https://github.com/openai/simple-evals/tree/main

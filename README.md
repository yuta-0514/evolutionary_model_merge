# Evolutionary Model Merge

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


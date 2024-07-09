import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
device = "cuda" # the device to load the model onto

# merge前
# model_id = "evol_merge_storage/input_models/shisa-gamma-7b-v1_4025154171"
model_id = "merge_mgsm_train"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)

inputs = tokenizer("問題:ジャネットのアヒルは1日に16個の卵を生みます。ジャネットは毎朝朝食の一環で3個を消費し、毎日4個使って友達向けにマフィンを焼きます。残りを市場で1個あたり2ドルの価格で売ります。彼女は毎日市場でいくら手に入れていますか?\n答え:", return_tensors="pt").to("cuda")
tokens = model.generate(
  **inputs,
  max_new_tokens=128,
  temperature=0.75,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))

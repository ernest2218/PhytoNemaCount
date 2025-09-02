import os
import random
import shutil
from pathlib import Path

# Caminhos
RAW_DIR = Path("raw_dataset")
IMG_EXT = [".jpg", ".png", ".jpeg"]

images = [f for f in RAW_DIR.iterdir() if f.suffix.lower() in IMG_EXT]
random.seed(42)
random.shuffle(images)

n_total = len(images)
n_train = int(0.8 * n_total)
n_val = int(0.1 * n_total)

train_files = images[:n_train]
val_files = images[n_train:n_train+n_val]
test_files = images[n_train+n_val:]

# Agora sim, os prints
print(f"Total de imagens encontradas: {len(images)}")
print(f"Treino: {len(train_files)}, Validação: {len(val_files)}, Teste: {len(test_files)}")

splits = {'train': train_files, 'val': val_files, 'test': test_files}

for split, files in splits.items():
    for f in files:
        # Copia imagem
        shutil.copy(f, Path(f"data/images/{split}/{f.name}"))
        # Copia label
        label_file = RAW_DIR / f"{f.stem}.txt"
        if label_file.exists():
            shutil.copy(label_file, Path(f"data/labels/{split}/{f.stem}.txt"))
        else:
            print(f"[AVISO] Anotação não encontrada para: {f.name}")

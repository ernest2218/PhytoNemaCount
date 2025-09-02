from ultralytics import YOLO
import os
from pathlib import Path
import cv2

# Caminho para o modelo treinado
model_path = "runs/nematoide_v1/weights/best.pt"

# Caminho para a pasta com novas imagens
images_folder = Path("new_images")

# Carregar modelo
model = YOLO(model_path)

# Garantir que existam imagens na pasta
image_files = list(images_folder.glob("*.[jp][pn]g"))  # pega .jpg, .jpeg, .png
if not image_files:
    print("Nenhuma imagem encontrada na pasta 'new_images'")
    exit()

# Criar a pasta de saída
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# Processar cada imagem
for img_path in image_files:
    # Rodar inferência
    results = model(img_path, conf=0.25)

    # Contar número de ovos detectados
    num_ovos = len(results[0].boxes)
    print(f"Imagem: {img_path.name} - Ovos detectados: {num_ovos}")

    # Gerar imagem com caixas desenhadas
    plot_img = results[0].plot()

    # Salvar a imagem com os resultados
    output_path = output_dir / img_path.name
    cv2.imwrite(str(output_path), plot_img)

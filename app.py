import streamlit as st
from PIL import Image
from ultralytics import YOLO
import tempfile
from pathlib import Path

# Carregar o modelo
model = YOLO("runs/nematoide_v1/weights/best.pt")
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

st.set_page_config(page_title="Detecção de ovos de nematóides", layout="centered")
st.title("🌐 PhytoNemaCount")
st.write("Contagem Descomplicada de Nematoides com IA e Visão Computacional")
st.caption("Desenvolvido com Streamlit e YOLO")
st.write("Este aplicativo permite identificar e contabilizar ovos de nematóides-das-galhas (Meloidogyne incognita) a partir de imagens de microscopia.")
st.markdown("**Carregue uma imagem para começar.**")

uploaded_file = st.file_uploader("Selecione uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Exibir imagem original
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = Path(tmp_file.name)

    st.image(Image.open(tmp_path), caption="Imagem original", use_container_width=True)

    # Sugestão de ação
    st.info("Clique abaixo para realizar a contagem de ovos de nematoide na imagem.")
    
    if st.button("🔍 Realizar contagem"):
        # Inferência
        results = model(tmp_path, conf=0.25)
        num_ovos = len(results[0].boxes)
        
        # Salvar imagem com marcações
        output_img_path = output_dir / uploaded_file.name
        results[0].save(filename=output_img_path)

        # Exibir resultado
        st.success(f"✅ Foram detectados **{num_ovos}** ovos de nematoide.")
        st.image(str(output_img_path), caption="Imagem com detecções", use_container_width=True)

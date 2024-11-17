# Etapa de compilación
FROM rust:bullseye as builder

# Instala wasm-pack y trunk para compilar Yew
RUN rustup target add wasm32-unknown-unknown \
    && cargo install --locked trunk

# Establece el directorio de trabajo
WORKDIR /app

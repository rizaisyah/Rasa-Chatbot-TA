# Gunakan image Rasa resmi
FROM rasa/rasa:3.6.21

# Salin semua file project ke dalam container
COPY . /app
WORKDIR /app

# (Opsional) install requirements tambahan untuk actions
# RUN pip install -r actions/requirements.txt

# Jalankan rasa
CMD ["run", "--enable-api", "--cors", "*"]

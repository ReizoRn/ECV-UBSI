# E-CV Digital — Abdurrazzaq & Afif Alfiansyah (Streamlit)

Proyek ini sudah disiapkan untuk di-deploy ke **Streamlit Community Cloud**. Website portofolio aslinya tetap menggunakan HTML, CSS, dan JavaScript; Streamlit menjadi pembungkus aplikasi dan menyajikan file statisnya.

## Isi penting
- `app.py` — entrypoint Streamlit.
- `requirements.txt` — dependensi Python.
- `.streamlit/config.toml` — mengaktifkan penyajian file statis.
- `static/index.html`, `static/style.css`, `static/script.js` — website utama.
- `static/foto/` — foto profil Abdurrazzaq dan Afif.
- `static/sertifikat/` — dokumen sertifikat PDF.
- File `index.html`, `style.css`, `script.js`, `foto/`, dan `sertifikat/` di folder utama juga dipertahankan untuk pratinjau lokal/editing.

## Cara menjalankan di komputer
1. Ekstrak ZIP.
2. Pastikan Python sudah terpasang.
3. Buka terminal/CMD pada folder proyek.
4. Jalankan:

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

5. Buka alamat lokal yang ditampilkan oleh Streamlit.

## Cara upload ke Streamlit.app
Streamlit Community Cloud melakukan deployment dari repositori GitHub, bukan dengan mengunggah ZIP langsung.

1. Ekstrak ZIP ini ke komputer.
2. Buat repositori baru di GitHub.
3. Unggah seluruh isi folder proyek ke repositori (termasuk folder `.streamlit` dan `static`). Pastikan `app.py` berada di root repositori.
4. Buka https://share.streamlit.io/ dan masuk menggunakan akun GitHub.
5. Pilih **Create app** / **Deploy an app**, lalu pilih repositori, branch, dan file utama `app.py`.
6. Klik **Deploy** dan tunggu proses selesai. Streamlit akan memberikan alamat `*.streamlit.app`.

## Cara mengedit
- Edit isi website pada `static/index.html` agar perubahan tampil di Streamlit.
- Edit desain pada `static/style.css`.
- Edit interaksi pada `static/script.js`.
- File sumber di folder utama disediakan untuk pengeditan/pratinjau lokal. Jika mengubah file sumber di folder utama, salin perubahan tersebut ke folder `static/` sebelum deploy.
- Foto dan sertifikat yang dipakai aplikasi berada di `static/foto/` dan `static/sertifikat/`. Pertahankan nama file dan struktur folder karena tautan HTML menggunakannya.

## Catatan
- Aplikasi ini adalah website portofolio statis yang dibungkus dengan Streamlit; tidak membutuhkan database atau backend.
- Setelah mengubah HTML/CSS, uji kembali tautan, menu, foto, dan PDF pada perangkat desktop dan ponsel.

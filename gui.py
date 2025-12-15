import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, date

from app.core import User, MotoCareApp


class MotoCareGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("MotoCare - Service Manager")
        self.root.geometry("900x600")

        # backend
        self.user = User("Liu")
        self.app = MotoCareApp(self.user)

        # build UI
        self._build_widgets()

    def _build_widgets(self):
        # ====== FRAME ATAS: FORM TAMBAH MOTOR ======
        frame_top = ttk.LabelFrame(self.root, text="Tambah Motor")
        frame_top.pack(fill="x", padx=10, pady=10)

        # Baris 1
        ttk.Label(frame_top, text="Plat").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.entry_plate = ttk.Entry(frame_top, width=15)
        self.entry_plate.grid(row=0, column=1, sticky="w", padx=5, pady=4)

        ttk.Label(frame_top, text="Merk").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.entry_brand = ttk.Entry(frame_top, width=18)
        self.entry_brand.grid(row=0, column=3, sticky="w", padx=5, pady=4)

        ttk.Label(frame_top, text="Tipe").grid(row=0, column=4, sticky="w", padx=5, pady=4)
        self.entry_model = ttk.Entry(frame_top, width=18)
        self.entry_model.grid(row=0, column=5, sticky="w", padx=5, pady=4)

        # Baris 2
        ttk.Label(frame_top, text="Tahun").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.entry_year = ttk.Entry(frame_top, width=15)
        self.entry_year.grid(row=1, column=1, sticky="w", padx=5, pady=4)

        ttk.Label(frame_top, text="KM sekarang").grid(row=1, column=2, sticky="w", padx=5, pady=4)
        self.entry_km = ttk.Entry(frame_top, width=18)
        self.entry_km.grid(row=1, column=3, sticky="w", padx=5, pady=4)

        btn_add_motor = ttk.Button(frame_top, text="Tambah Motor", command=self.add_motorcycle)
        btn_add_motor.grid(row=1, column=5, sticky="e", padx=5, pady=4)

        for i in range(6):
            frame_top.columnconfigure(i, weight=1)

        # ====== FRAME TENGAH: LIST MOTOR ======
        frame_mid = ttk.LabelFrame(self.root, text="Daftar Motor")
        frame_mid.pack(fill="both", expand=False, padx=10, pady=5)

        frame_mid_inner = ttk.Frame(frame_mid)
        frame_mid_inner.pack(fill="both", expand=True, padx=5, pady=5)

        self.list_motors = tk.Listbox(frame_mid_inner, height=6, exportselection=False)
        self.list_motors.pack(side="left", fill="both", expand=True, padx=(0, 0), pady=5)

        scrollbar_motors = ttk.Scrollbar(frame_mid_inner, orient="vertical", command=self.list_motors.yview)
        scrollbar_motors.pack(side="right", fill="y", padx=(0, 0), pady=5)
        self.list_motors.config(yscrollcommand=scrollbar_motors.set)

        self.list_motors.bind("<<ListboxSelect>>", self.on_motor_select)

        # tombol hapus motor di bawah list
        btn_delete_motor = ttk.Button(frame_mid, text="Hapus Motor", command=self.delete_motorcycle)
        btn_delete_motor.pack(fill="x", padx=5, pady=(0, 5))


        # ====== FRAME BAWAH: SERVIS ======
        frame_bottom = ttk.LabelFrame(self.root, text="Servis Motor Terpilih")
        frame_bottom.pack(fill="both", expand=True, padx=10, pady=10)

        # kiri: form tambah servis
        frame_service_form = ttk.Frame(frame_bottom)
        frame_service_form.pack(side="top", fill="x", padx=5, pady=5)

        # Baris 1
        ttk.Label(frame_service_form, text="Tanggal (YYYY-MM-DD)").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.entry_service_date = ttk.Entry(frame_service_form, width=15)
        self.entry_service_date.grid(row=0, column=1, sticky="w", padx=5, pady=4)
        self.entry_service_date.insert(0, date.today().strftime("%Y-%m-%d"))

        ttk.Label(frame_service_form, text="KM").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.entry_service_km = ttk.Entry(frame_service_form, width=10)
        self.entry_service_km.grid(row=0, column=3, sticky="w", padx=5, pady=4)

        # Baris 2
        ttk.Label(frame_service_form, text="Jenis Servis").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.entry_service_type = ttk.Entry(frame_service_form)
        self.entry_service_type.grid(row=1, column=1, columnspan=3, sticky="we", padx=5, pady=4)

        # Baris 3
        ttk.Label(frame_service_form, text="Biaya (Rp)").grid(row=2, column=0, sticky="w", padx=5, pady=4)
        self.entry_service_cost = ttk.Entry(frame_service_form, width=15)
        self.entry_service_cost.grid(row=2, column=1, sticky="w", padx=5, pady=4)

        ttk.Label(frame_service_form, text="Catatan").grid(row=2, column=2, sticky="w", padx=5, pady=4)
        self.entry_service_notes = ttk.Entry(frame_service_form)
        self.entry_service_notes.grid(row=2, column=3, sticky="we", padx=5, pady=4)

        # Baris 4 tombol
        btn_add_service = ttk.Button(frame_service_form, text="Tambah Servis", command=self.add_service)
        btn_add_service.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        btn_update_service = ttk.Button(frame_service_form, text="Update Servis", command=self.update_service)
        btn_update_service.grid(row=3, column=3, padx=5, pady=5, sticky="e")

        for i in range(4):
            frame_service_form.columnconfigure(i, weight=1)

        # kanan: list histori servis
        frame_service_list = ttk.Frame(frame_bottom)
        frame_service_list.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

        ttk.Label(frame_service_list, text="Histori Servis:").pack(anchor="w", padx=5)

        self.list_services = tk.Listbox(frame_service_list, exportselection=False)
        self.list_services.pack(side="left", fill="both", expand=True, padx=(5, 0), pady=5)

        scrollbar_services = ttk.Scrollbar(frame_service_list, orient="vertical", command=self.list_services.yview)
        scrollbar_services.pack(side="right", fill="y", padx=(0, 5), pady=5)
        self.list_services.config(yscrollcommand=scrollbar_services.set)
        self.list_services.bind("<<ListboxSelect>>", self.on_service_select)

    # ================== LOGIC ==================

    def add_motorcycle(self):
        plate = self.entry_plate.get().strip()
        brand = self.entry_brand.get().strip()
        model = self.entry_model.get().strip()
        year_text = self.entry_year.get().strip()
        km_text = self.entry_km.get().strip()

        if not plate or not brand or not model or not year_text or not km_text:
            messagebox.showerror("Error", "Semua field motor harus diisi.")
            return

        try:
            year = int(year_text)
            current_km = int(km_text)
        except ValueError:
            messagebox.showerror("Error", "Tahun dan KM harus berupa angka.")
            return

        # cek duplikat plat
        for mc in self.user.motorcycles:
            if mc.plate == plate:
                messagebox.showerror("Error", f"Motor dengan plat {plate} sudah ada.")
                return

        self.app.add_motorcycle(plate, brand, model, year, current_km)
        self.refresh_motor_list()

    def delete_motorcycle(self):
        plate = self.get_selected_plate()
        if plate is None:
            messagebox.showerror("Error", "Pilih motor yang akan dihapus.")
            return

        if not messagebox.askyesno(
            "Konfirmasi",
            f"Hapus motor dengan plat {plate}? Semua histori servis akan ikut terhapus."
        ):
            return

        try:
            self.app.remove_motorcycle(plate)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # refresh tampilan
        self.refresh_motor_list()
        self.list_services.delete(0, tk.END)

        # clear input
        self.entry_plate.delete(0, tk.END)
        self.entry_brand.delete(0, tk.END)
        self.entry_model.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_km.delete(0, tk.END)

    def refresh_motor_list(self):
        self.list_motors.delete(0, tk.END)
        for mc in self.user.motorcycles:
            self.list_motors.insert(tk.END, mc.get_info())

    def on_motor_select(self, event):
        selection = self.list_motors.curselection()
        if not selection:
            return
        index = selection[0]
        mc = self.user.motorcycles[index]
        self.refresh_service_list(mc.plate)

    def refresh_service_list(self, plate: str):
        self.list_services.delete(0, tk.END)
        history = self.app.get_service_history(plate)
        for rec in history:
            self.list_services.insert(tk.END, str(rec))

    def get_selected_plate(self):
        selection = self.list_motors.curselection()
        if not selection:
            return None
        index = selection[0]
        mc = self.user.motorcycles[index]
        return mc.plate

    def add_service(self):
        plate = self.get_selected_plate()
        if plate is None:
            messagebox.showerror("Error", "Pilih motor terlebih dahulu.")
            return

        date_text = self.entry_service_date.get().strip()
        km_text = self.entry_service_km.get().strip()
        service_type = self.entry_service_type.get().strip()
        cost_text = self.entry_service_cost.get().strip()
        notes = self.entry_service_notes.get().strip()

        if not date_text or not km_text or not service_type or not cost_text:
            messagebox.showerror("Error", "Tanggal, KM, Jenis Servis, dan Biaya harus diisi.")
            return

        try:
            date_obj = datetime.strptime(date_text, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Format tanggal harus YYYY-MM-DD.")
            return

        try:
            km = int(km_text)
            cost = float(cost_text)
        except ValueError:
            messagebox.showerror("Error", "KM harus integer dan biaya harus angka.")
            return

        try:
            self.app.add_service_to_motorcycle(plate, date_obj, km, service_type, cost, notes)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.refresh_service_list(plate)

        # optional: kosongkan beberapa field
        self.entry_service_km.delete(0, tk.END)
        self.entry_service_type.delete(0, tk.END)
        self.entry_service_cost.delete(0, tk.END)
        self.entry_service_notes.delete(0, tk.END)

    def on_service_select(self, event):
        plate = self.get_selected_plate()
        if plate is None:
            return

        selection = self.list_services.curselection()
        if not selection:
            return

        index = selection[0]
        history = self.app.get_service_history(plate)
        if index < 0 or index >= len(history):
            return

        rec = history[index]

        # isi form berdasarkan record yang dipilih
        self.entry_service_date.delete(0, tk.END)
        self.entry_service_date.insert(0, rec._date.strftime("%Y-%m-%d"))

        self.entry_service_km.delete(0, tk.END)
        self.entry_service_km.insert(0, str(rec._km))

        self.entry_service_type.delete(0, tk.END)
        self.entry_service_type.insert(0, rec._service_type)

        self.entry_service_cost.delete(0, tk.END)
        self.entry_service_cost.insert(0, str(rec._cost))

        self.entry_service_notes.delete(0, tk.END)
        self.entry_service_notes.insert(0, rec._notes)

    def update_service(self):
        plate = self.get_selected_plate()
        if plate is None:
            messagebox.showerror("Error", "Pilih motor terlebih dahulu.")
            return

        selection = self.list_services.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih record servis yang akan diupdate.")
            return

        index = selection[0]

        date_text = self.entry_service_date.get().strip()
        km_text = self.entry_service_km.get().strip()
        service_type = self.entry_service_type.get().strip()
        cost_text = self.entry_service_cost.get().strip()
        notes = self.entry_service_notes.get().strip()

        if not date_text or not km_text or not service_type or not cost_text:
            messagebox.showerror("Error", "Tanggal, KM, Jenis Servis, dan Biaya harus diisi.")
            return

        try:
            date_obj = datetime.strptime(date_text, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Format tanggal harus YYYY-MM-DD.")
            return

        try:
            km = int(km_text)
            cost = float(cost_text)
        except ValueError:
            messagebox.showerror("Error", "KM harus integer dan biaya harus angka.")
            return

        try:
            self.app.update_service_for_motorcycle(plate, index, date_obj, km, service_type, cost, notes)
        except (ValueError, IndexError) as e:
            messagebox.showerror("Error", str(e))
            return

        self.refresh_service_list(plate)
        messagebox.showinfo("Sukses", "Data servis berhasil diupdate.")



if __name__ == "__main__":
    root = tk.Tk()
    gui = MotoCareGUI(root)
    root.mainloop()

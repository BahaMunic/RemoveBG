import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def remove_background(input_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")

        datas = img.getdata()

        new_data = []
        for item in datas:
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if output_path:
            img.save(output_path, "PNG")
            messagebox.showinfo("نجاح", f"تم حفظ الصورة في: {output_path}")

    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء معالجة {input_path}: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.tiff")])
    if file_path:
        remove_background(file_path)

def exit_app():
    root.quit()

def show_about():
    messagebox.showinfo("حول", "برنامج سريع وفعال لإزالة الخلفيات عن صور التواقيع على نظام ويندوز. يدعم مجموعة واسعة من صيغ الصور ويحفظ التواقيع بدون خلفية وذلك لضمان الخصوصية وعدم رفع التواقيع الرسمية على مواقع خارجية ")

def show_license():
    messagebox.showinfo("ترخيص", "هذا البرنامج مٌرخص بموجب رخصة جنو العمومية العامة الإصدار 2 (GPLv2). يمكنك إعادة توزيعه وتعديله وفقًا للشروط الواردة في الرخصة.  \n لمزيد من المعلومات، يمكن الاطلاع على تفاصيل التراخيص العمومية بالرابط https://www.gnu.org/licenses/")

root = tk.Tk()
root.title("مزيل خلفية التواقيع")
root.geometry("400x300")

# Create menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="خروج", command=exit_app)
menu_bar.add_cascade(label="ملف", menu=file_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="حول", command=show_about)
help_menu.add_command(label="ترخيص", command=show_license)
menu_bar.add_cascade(label="حول", menu=help_menu)

root.config(menu=menu_bar)

button = tk.Button(root, text="اختر ملف صورة", command=browse_file)
button.pack(expand=True)

# Add label for agency name
agency_label = tk.Label(root, text='تم بواسطة وكالة التحول الرقمي بأمانة منطقة الباحة', justify='right', wraplength=300)
agency_label.pack(side='bottom', pady=10)

root.mainloop()

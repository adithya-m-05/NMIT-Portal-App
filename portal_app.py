import tkinter as tk
from tkinter import messagebox
import json, os, threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PROFILE_FILE = "profiles.json"

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_profiles():
    with open(PROFILE_FILE, "w") as f:
        json.dump(profiles, f, indent=4)

profiles = load_profiles()

# 🎯 COLORS (minimal aesthetic)
BG = "#121212"
CARD = "#1E1E1E"
ACCENT = "#4CAF50"
TEXT = "#E0E0E0"
SUBTEXT = "#A0A0A0"

def open_portal(profile):
    status_label.config(text="Opening portal...", fg=ACCENT)

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.page_load_strategy = 'eager'

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 8)

        driver.get("https://nitte.edu.in/nmit/")
        driver.execute_script("submitparentportaldata();")

        wait.until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='USN']"))).send_keys(profile["usn"])

        day = Select(wait.until(EC.presence_of_element_located((By.XPATH, "(//select)[1]"))))
        month = Select(wait.until(EC.presence_of_element_located((By.XPATH, "(//select)[2]"))))
        year = Select(wait.until(EC.presence_of_element_located((By.XPATH, "(//select)[3]"))))

        day.select_by_visible_text(profile["day"])
        month.select_by_visible_text(profile["month"])
        year.select_by_visible_text(profile["year"])

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='submit' and @value='Login']")
        )).click()

        status_label.config(text="Logged in successfully ✅", fg=ACCENT)

    except Exception as e:
        status_label.config(text="Error ❌", fg="red")
        messagebox.showerror("Error", str(e))


def login_selected():
    selected = profile_list.get(tk.ACTIVE)
    if not selected:
        return
    threading.Thread(target=open_portal, args=(profiles[selected],)).start()


def add_profile():
    name = name_entry.get().strip()
    usn = usn_entry.get().strip()

    if not name or not usn:
        messagebox.showwarning("Error", "Fill all fields")
        return

    profiles[name] = {
        "usn": usn,
        "day": day_var.get(),
        "month": month_var.get(),
        "year": year_var.get()
    }

    save_profiles()
    refresh_list()


def delete_profile():
    selected = profile_list.get(tk.ACTIVE)
    if selected in profiles:
        del profiles[selected]
        save_profiles()
        refresh_list()


def refresh_list():
    profile_list.delete(0, tk.END)
    for name in profiles:
        profile_list.insert(tk.END, name)


# 🖥️ GUI
root = tk.Tk()
root.title("NMIT Portal")
root.geometry("600x450")
root.configure(bg=BG)

# TITLE
tk.Label(root, text="NMIT Portal", font=("Segoe UI", 20, "bold"),
         bg=BG, fg=TEXT).pack(pady=15)

# MAIN FRAME
main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=20)

# LEFT CARD (profiles)
left = tk.Frame(main, bg=CARD)
left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

tk.Label(left, text="Profiles", font=("Segoe UI", 12, "bold"),
         bg=CARD, fg=TEXT).pack(pady=10)

profile_list = tk.Listbox(left, bg="#2A2A2A", fg=TEXT,
                          selectbackground=ACCENT, relief="flat")
profile_list.pack(fill="both", expand=True, padx=10, pady=5)

tk.Button(left, text="Login", bg=ACCENT, fg="white",
          relief="flat", command=login_selected).pack(pady=5, ipadx=10)

tk.Button(left, text="Delete", bg="#444", fg="white",
          relief="flat", command=delete_profile).pack(pady=5, ipadx=10)

# RIGHT CARD (add profile)
right = tk.Frame(main, bg=CARD)
right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(right, text="Add Profile", font=("Segoe UI", 12, "bold"),
         bg=CARD, fg=TEXT).pack(pady=10)

name_entry = tk.Entry(right, bg="#2A2A2A", fg=TEXT, relief="flat")
name_entry.pack(pady=5, padx=10, fill="x")
name_entry.insert(0, "Profile Name")

usn_entry = tk.Entry(right, bg="#2A2A2A", fg=TEXT, relief="flat")
usn_entry.pack(pady=5, padx=10, fill="x")
usn_entry.insert(0, "USN")

day_var = tk.StringVar(value="1")
month_var = tk.StringVar(value="July")
year_var = tk.StringVar(value="2005")

tk.Entry(right, textvariable=day_var, bg="#2A2A2A", fg=TEXT, relief="flat").pack(pady=2, padx=10, fill="x")
tk.Entry(right, textvariable=month_var, bg="#2A2A2A", fg=TEXT, relief="flat").pack(pady=2, padx=10, fill="x")
tk.Entry(right, textvariable=year_var, bg="#2A2A2A", fg=TEXT, relief="flat").pack(pady=2, padx=10, fill="x")

tk.Button(right, text="Add Profile", bg=ACCENT, fg="white",
          relief="flat", command=add_profile).pack(pady=10, ipadx=10)

# STATUS
status_label = tk.Label(root, text="Status: Ready",
                        bg=BG, fg=SUBTEXT, font=("Segoe UI", 10))
status_label.pack(pady=10)

refresh_list()
root.mainloop()
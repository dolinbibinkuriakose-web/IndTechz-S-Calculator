import tkinter as tk
from tkinter import messagebox
import math
import re

class SpideyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("IndTechz S-Calculator: Iron Spider Edition")
        self.root.geometry("400x750")
        self.root.configure(bg="#1a1a1a")

        self.expression = ""
        self.new_calculation = False
        self.is_pinned = False 
        self.menu_open = False

        # Main container
        self.main_container = tk.Frame(self.root, bg="#1a1a1a")
        self.main_container.pack(expand=True, fill="both")

        self.setup_styles()
        self.show_home_page()

    def setup_styles(self):
        # Muted Iron Spider Suit Palette
        self.colors = {
            'bg': "#1a1a1a",
            'iron_red': "#b33939",      # Muted red
            'gold_glow': "#d1a054",     # Softened gold
            'stark_blue': "#54a0ff",    # Dusty blue
            'text': "#dcdde1",          # Soft white
            'screen_bg': "#2f3640",     # Charcoal screen
            'btn_bg': "#222f3e",        # Deep navy/grey buttons
            'menu_bg': "#222f3e"
        }

    def toggle_float(self):
        """Toggles 'Always on Top' functionality."""
        self.is_pinned = not self.is_pinned
        self.root.attributes("-topmost", self.is_pinned)
        if hasattr(self, 'pin_btn'):
            active_color = self.colors['gold_glow'] if self.is_pinned else "#7f8c8d"
            self.pin_btn.config(fg=active_color)

    def toggle_menu(self):
        """Toggles the feature menu overlay."""
        if not self.menu_open:
            self.menu_frame = tk.Frame(self.root, bg=self.colors['menu_bg'], bd=2, relief="ridge")
            self.menu_frame.place(x=50, y=100, width=300, height=500)
            
            tk.Label(self.menu_frame, text="IndTechz S-Calculator", font=("Impact", 16), 
                     bg=self.colors['menu_bg'], fg=self.colors['stark_blue']).pack(pady=10)
            
            features = [
                "• Trigonometry (sin, cos, tan)",
                "• Inverse Trig (asin, acos, atan)",
                "• Factorials (x!)",
                "• Power Functions (xʸ)",
                "• Combinations (nCr)",
                "• Permutations (nPr)",
                "• Constants (π, e)",
                "• Auto-Parentheses Balancing",
                "• Pin to Top (📌)",
                "• Keyboard Support"
            ]
            
            for f in features:
                tk.Label(self.menu_frame, text=f, font=("Arial", 10, "bold"), 
                         bg=self.colors['menu_bg'], fg=self.colors['text'], anchor="w").pack(fill="x", padx=20, pady=2)
            
            tk.Button(self.menu_frame, text="CLOSE MENU", font=("Arial Black", 10),
                      bg=self.colors['iron_red'], fg="white", command=self.toggle_menu).pack(pady=20)
            self.menu_open = True
        else:
            self.menu_frame.destroy()
            self.menu_open = False

    def show_home_page(self):
        """Displays the home screen with shortcuts."""
        for widget in self.main_container.winfo_children(): 
            widget.destroy()
            
        home_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        home_frame.pack(expand=True, fill="both", padx=30)
        
        tk.Label(home_frame, text="IndTechz S-Calculator", font=("Impact", 24), 
                 bg=self.colors['bg'], fg=self.colors['gold_glow']).pack(pady=(40, 20))
        
        shortcuts = [
            ("Enter", "Calculate Result"),
            ("BackSpace", "Delete Last Char"),
            ("Escape", "All Clear (AC)"),
            ("P", "Insert Pi (π)"),
            ("E", "Insert Euler's (e)"),
            ("s / c / t", "sin / cos / tan"),
            ("S / C / T", "asin / acos / atan"),
            ("!", "Factorial"),
            ("* or X", "Multiplication")
        ]
        
        shortcut_box = tk.Frame(home_frame, bg=self.colors['btn_bg'], padx=15, pady=15)
        shortcut_box.pack(fill="x", pady=20)
        
        for key, desc in shortcuts:
            row = tk.Frame(shortcut_box, bg=self.colors['btn_bg'])
            row.pack(fill="x", pady=2)
            tk.Label(row, text=key, font=("Consolas", 10, "bold"), bg=self.colors['btn_bg'], fg=self.colors['gold_glow'], width=10, anchor="w").pack(side="left")
            tk.Label(row, text=desc, font=("Arial", 10), bg=self.colors['btn_bg'], fg=self.colors['text'], anchor="w").pack(side="left")

        tk.Button(home_frame, text="SWING TO CALCULATOR", font=("Arial Black", 12),
                  bg=self.colors['iron_red'], fg="white", bd=0, padx=20, pady=10,
                  cursor="hand2", command=self.show_calculator_page).pack(pady=30)

    def show_calculator_page(self):
        for widget in self.main_container.winfo_children(): 
            widget.destroy()

        # Header with Menu, Home, and Pin
        header = tk.Frame(self.main_container, bg=self.colors['bg'])
        header.pack(fill="x", padx=20, pady=(20, 5))
        
        tk.Button(header, text="☰", font=("Arial", 14, "bold"), bg=self.colors['bg'], 
                  fg=self.colors['stark_blue'], bd=0, cursor="hand2", command=self.toggle_menu).pack(side="left")
        
        tk.Button(header, text="🏠", font=("Arial", 14), bg=self.colors['bg'], 
                  fg=self.colors['gold_glow'], bd=0, cursor="hand2", command=self.show_home_page).pack(side="left", padx=5)
        
        tk.Label(header, text="IRON SPIDER // S-CALC", 
                 font=("Impact", 14), bg=self.colors['bg'], fg=self.colors['gold_glow']).pack(side="left", padx=10)
        
        self.pin_btn = tk.Button(header, text="📌", font=("Arial", 12), bg=self.colors['bg'], 
                                 fg="#7f8c8d", bd=0, cursor="hand2", command=self.toggle_float)
        self.pin_btn.pack(side="right")

        # Screen
        screen_frame = tk.Frame(self.main_container, bg=self.colors['stark_blue'], padx=1, pady=1)
        screen_frame.pack(pady=10, fill="x", padx=20)
        
        inner_screen = tk.Frame(screen_frame, bg=self.colors['screen_bg'])
        inner_screen.pack(fill="both")

        self.screen = tk.Entry(inner_screen, font=("Consolas", 28), bg=self.colors['screen_bg'], 
                               fg=self.colors['stark_blue'], justify="right", bd=0, relief="flat",
                               insertbackground=self.colors['stark_blue'])
        self.screen.pack(fill="x", ipady=25, padx=10)
        self.screen.insert(0, "SYSTEM_READY")
        self.screen.bind("<Key>", lambda e: "break")

        # Keypad
        self.keypad = tk.Frame(self.main_container, bg=self.colors['bg'])
        self.keypad.pack(expand=True, fill="both", padx=15, pady=10)

        buttons = [
            ('sin', 0, 0, 'sci'), ('cos', 0, 1, 'sci'), ('tan', 0, 2, 'sci'), ('x!', 0, 3, 'sci'),
            ('asin', 1, 0, 'sci'), ('acos', 1, 1, 'sci'), ('atan', 1, 2, 'sci'), ('xʸ', 1, 3, 'sci'),
            ('nCr', 2, 0, 'sci'), ('nPr', 2, 1, 'sci'), ('(', 2, 2, 'op'), (')', 2, 3, 'op'),
            ('7', 3, 0, 'num'), ('8', 3, 1, 'num'), ('9', 3, 2, 'num'), ('DEL', 3, 3, 'del'),
            ('4', 4, 0, 'num'), ('5', 4, 1, 'num'), ('6', 4, 2, 'num'), ('AC', 4, 3, 'del'),
            ('1', 5, 0, 'num'), ('2', 5, 1, 'num'), ('3', 5, 2, 'num'), ('+', 5, 3, 'op'),
            ('0', 6, 0, 'num'), ('.', 6, 1, 'num'), ('x', 6, 2, 'op'), ('-', 6, 3, 'op'),
            ('π', 7, 0, 'sci'), ('e', 7, 1, 'sci'), ('/', 7, 2, 'op'), ('=', 7, 3, 'eq'),
        ]

        for (text, r, c, b_type) in buttons:
            cmd = lambda t=text: self.on_click(t)
            
            bg_color = self.colors['btn_bg']
            fg_color = self.colors['text']
            
            if b_type == 'eq': 
                bg_color = self.colors['gold_glow']
                fg_color = "black"
            elif b_type == 'del':
                fg_color = self.colors['iron_red']
            elif b_type == 'op':
                fg_color = self.colors['stark_blue']
            elif b_type == 'sci':
                fg_color = self.colors['gold_glow']

            btn = tk.Button(self.keypad, text=text, font=("Arial Black", 10),
                            bg=bg_color, fg=fg_color, 
                            activebackground=self.colors['stark_blue'], 
                            activeforeground="black",
                            bd=0, relief="flat", cursor="hand2",
                            command=cmd)
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
            
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#485460"))
            btn.bind("<Leave>", lambda e, b=btn, bg=bg_color: b.config(bg=bg))

            self.keypad.grid_columnconfigure(c, weight=1)
            self.keypad.grid_rowconfigure(r, weight=1)

        self.root.bind("<Key>", self.keyboard_input)

    def keyboard_input(self, event):
        char = event.char
        if event.keysym == "Return": self.on_click("=")
        elif event.keysym == "BackSpace": self.on_click("DEL")
        elif event.keysym == "Escape": self.on_click("AC")
        elif char in "0123456789.+-/()": self.on_click(char)
        elif char.lower() in ["*", "x"]: self.on_click("x")
        elif char == "p": self.on_click("π")
        elif char == "e": self.on_click("e")
        elif char == "s": self.on_click("sin")
        elif char == "c": self.on_click("cos")
        elif char == "t": self.on_click("tan")
        elif char == "S": self.on_click("asin") # Shift+s
        elif char == "C": self.on_click("acos") # Shift+c
        elif char == "T": self.on_click("atan") # Shift+t
        elif char == "!": self.on_click("x!")

    def on_click(self, char):
        if self.new_calculation and char not in ['+', '-', 'x', '/', 'xʸ', '=']:
            self.expression = ""
        self.new_calculation = False
        
        if char == "AC": self.expression = ""
        elif char == "DEL": self.expression = self.expression[:-1]
        elif char == "=": self.calculate()
        else:
            if char in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']: self.expression += f"{char}("
            elif char == 'xʸ': self.expression += "**"
            elif char == 'x!': self.expression += "!"
            else: self.expression += str(char)
        self.update_display()

    def calculate(self):
        try:
            is_radian = "π" in self.expression
            s_dict = {
                'sin': lambda x: math.sin(x) if is_radian else math.sin(math.radians(x)),
                'cos': lambda x: math.cos(x) if is_radian else math.cos(math.radians(x)),
                'tan': lambda x: math.tan(x) if is_radian else math.tan(math.radians(x)),
                'asin': lambda x: math.asin(x) if is_radian else math.degrees(math.asin(x)),
                'acos': lambda x: math.acos(x) if is_radian else math.degrees(math.acos(x)),
                'atan': lambda x: math.atan(x) if is_radian else math.degrees(math.atan(x)),
                'pi': math.pi, 'e': math.e
            }
            expr = self.expression.replace('x', '*').replace('π', 'pi')
            while '!' in expr: expr = re.sub(r'(\d+)!', r'math.factorial(\1)', expr)
            while 'nCr' in expr: expr = re.sub(r'(\d+)nCr(\d+)', r'math.comb(\1,\2)', expr)
            while 'nPr' in expr: expr = re.sub(r'(\d+)nPr(\d+)', r'math.perm(\1,\2)', expr)
            
            open_c, close_c = expr.count('('), expr.count(')')
            if open_c > close_c: expr += ')' * (open_c - close_c)
            
            result = eval(expr, {"__builtins__": None, "math": math}, s_dict)
            self.expression = str(round(result, 10))
            self.new_calculation = True
        except Exception:
            self.expression = "STARK_SYS_ERR"
            self.new_calculation = True
        self.update_display()

    def update_display(self):
        if hasattr(self, 'screen'):
            self.screen.delete(0, tk.END)
            self.screen.insert(0, self.expression if self.expression else "SYSTEM_READY")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpideyCalculator(root)
    root.mainloop()
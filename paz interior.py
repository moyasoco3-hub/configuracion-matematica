    "#Grafico polimonial grado 4 \n",
    "import numpy as np\n",
    "import matplotlib.pyplot as ply \n",
    "\n",
    "# Definir el polinomio: P(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e\n",
    "def P(x, a, b, c, d, e):\n",
    "    return a*x**4 + b*x**3 + c*x**2 + d*x + e\n",
    "\n",
    "# Coeficientes del polinomio (puedes cambiarlos)\n",
    "a, b, c, d, e = 1, -3, 2, 5, -4\n",
    "# Rango de valores de x\n",
    "x_vals = np.linspace(-5, 5, 400)\n",
    "\n",
    "# Evaluar el polinomio en cada x\n",
    "y_vals = P(x_vals, a, b, c, d, e)\n",
    "\n",
    "# Crear la grafica \n",
    "plt.plot(x_vals, y_vals, label=f'P(x) = {a}x⁴ + {b}x³ + {c}x² + {d}x + {e}')\n",
    "plt.axhline(0, color='black', linewidth=1) # Linea horizontal en y=0\n",
    "plt.axvline(0, color='black', linewith=1) # Linea vertical en x=0\n",
    "plt.grid(True, linestyle='--', alpha=0.6)\n",
    "plt.legend()\n",
    "plt.xlabel(\"x\")\n",
    "plt.ylabel(\"P(x)\")\n",
    "plt.title(\"Grafico del polinomio de grado 4\")\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

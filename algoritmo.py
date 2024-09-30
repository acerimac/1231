{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM7W6tUwL82Gv/uJs2sW+AD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/acerimac/1231/blob/main/algoritmo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HtqcJpWgTV1E"
      },
      "outputs": [],
      "source": [
        "nome_cidade = \"São Paulo\"\n",
        "numero_habitantes = 12176866\n",
        "estado = \"São Paulo\"\n",
        "tamanho_cidade_km2 = 1521.11\n",
        "possui_metro = True\n",
        "\n",
        "tempo_gasto = input(\"Informe o tempo gasto (em horas): \")\n",
        "velocidade_media = input(\"Informe a velocidade média (em km/h): \")\n",
        "tempo_gasto = float(tempo_gasto)\n",
        "velocidade_media = float(velocidade_media)\n",
        "\n",
        "\n",
        "distancia = velocidade_media * tempo_gasto\n",
        "combustivel_gasto = distancia\n",
        "\n",
        "\n",
        "print(\"Quantidade de combustível gasto:\", combustivel_gasto)"
      ]
    }
  ]
}
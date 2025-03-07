{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPKyz6VfofF5f27j+aFyVrN",
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
        "<a href=\"https://colab.research.google.com/github/Agum82/Praktikum_Search_Algoritthms/blob/main/dfs.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JmdE9EsLZg7D",
        "outputId": "8330e059-f6ca-451f-ecea-b46f47ba6393"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Berikut adalah Penelusuran Depth First (dimulai dari node 2 )\n",
            "2 0 1 3 "
          ]
        }
      ],
      "source": [
        "from collections import defaultdict\n",
        "\n",
        "class Graph:\n",
        "  def __init__(self):\n",
        "    self.graph = defaultdict(list)\n",
        "\n",
        "  def addEdge(self, u, v):\n",
        "    self.graph[u].append(v)\n",
        "\n",
        "  def DFSUTil(self, v, visited):\n",
        "   visited.add(v)\n",
        "   print(v, end=' ')\n",
        "\n",
        "   for neighbour in self.graph[v]:\n",
        "     if neighbour not in visited:\n",
        "       self.DFSUTil(neighbour, visited)\n",
        "\n",
        "  def DFS(self, v):\n",
        "    visited = set()\n",
        "    self.DFSUTil(v, visited)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  g = Graph()\n",
        "  g.addEdge(0, 1)\n",
        "  g.addEdge(0, 2)\n",
        "  g.addEdge(1, 2)\n",
        "  g.addEdge(2, 0)\n",
        "  g.addEdge(2, 3)\n",
        "  g.addEdge(3, 3)\n",
        "\n",
        "  print(\"Berikut adalah Penelusuran Depth First (dimulai dari node 2 )\")\n",
        "  g.DFS(2)"
      ]
    }
  ]
}
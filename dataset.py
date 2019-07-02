{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled15.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AdoniaMbarebaki/Exercise1/blob/master/dataset.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r-RzTWucFx5d",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        },
        "outputId": "492898bf-295d-4eb8-cef4-3db00c7a670d"
      },
      "source": [
        "from sklearn.neural_network.multilayer_perceptron import MLPClassifier\n",
        "from sklearn import datasets\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "iris = datasets.load_iris()\n",
        "data = iris.data\n",
        "labels = iris.target\n",
        "\n",
        "mlp = MLPClassifier(random_state = 1, max_iter = 1000)\n",
        "mlp.fit (data,labels)\n",
        "pred = mlp.predict(data)\n",
        "\n",
        "print()\n",
        "print('Accuracy: %.2F' %accuracy_score(labels, pred))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "Accuracy: 0.98\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "06rHP6wAIoix",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
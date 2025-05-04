from nn_vs_nn1 import DialogNN


if __name__ == "__main__":
    print("Выберите нейросеть1/2:\n· gpt-3.5-turbo\n· deepseek-v3\n")
    nn1 = input("Введите нейросеть 1: ")
    nn2 = input("Введите нейросеть 2: ")

    new_dialog = DialogNN(nn1, nn2)
    new_dialog.dialog()

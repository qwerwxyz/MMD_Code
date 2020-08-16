import matplotlib.pyplot as plt

if __name__ == '__main__':
    v2_trainloss = [1.151074262,0.916629575,0.885377961,0.870925433,0.86170251,0.854922923,0.848338437,0.838338437,0.8364463,0.8308695065101188,0.8266530903629373]

    v2_validloss = [0.984234,0.90565, 0.897564,0.884573,0.882433,0.880356,0.885166,0.884914,0.888592,0.898891,0.896911]

    v1_trainloss = [2.201383216816683, 1.872286355239716, 1.772703]
    v1_validloss = [2.051658, 1.887203, 1.828919]
    plt.plot(v2_trainloss, label="v2trainloss")
    plt.plot(v2_validloss, label="v2validloss")
    plt.plot(v1_trainloss, label="v1trainloss", linestyle='--')
    plt.plot(v1_validloss, label="v1validloss", linestyle='--')
    plt.legend()
    plt.xlabel('epoch')
    plt.ylabel('value')
    plt.show()


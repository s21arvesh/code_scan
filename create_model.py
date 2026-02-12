import pickle

class Demo:
    def __reduce__(self):
        return (print, ("This is a test payload",))

pickle.dump(Demo(), open("model.pkl", "wb"))

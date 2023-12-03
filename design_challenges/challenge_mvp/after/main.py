from View import GuiView
from Presenter import DataPresenter
from Model import DataModel


def main() -> None:
    model = DataModel()
    presenter = DataPresenter(model)
    gui = GuiView(presenter)
    gui.run()


if __name__ == "__main__":
    main()

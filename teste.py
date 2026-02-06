from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.utils import platform
import webbrowser

KV = """
BoxLayout:
    orientation: "vertical"
    padding: dp(16)
    spacing: dp(12)

    Label:
        text: "Bot de Redação (Android)"
        font_size: "22sp"
        size_hint_y: None
        height: self.texture_size[1]

    Label:
        id: status_label
        text: app.status_message
        size_hint_y: None
        height: self.texture_size[1] + dp(8)
        color: (0.9, 0.95, 1, 1)

    TextInput:
        id: text_input
        hint_text: "Digite sua redação aqui..."
        multiline: True

    GridLayout:
        cols: 2
        size_hint_y: None
        height: dp(48)
        spacing: dp(8)

        Button:
            text: "Abrir ChatGPT"
            on_release: app.open_url("https://chat.openai.com")

        Button:
            text: "Abrir QuillBot"
            on_release: app.open_url("https://quillbot.com")

    GridLayout:
        cols: 2
        size_hint_y: None
        height: dp(48)
        spacing: dp(8)

        Button:
            text: "Copiar Texto"
            on_release: app.copy_text(text_input.text)

        Button:
            text: "Compartilhar Texto"
            on_release: app.share_text(text_input.text)
"""


class AndroidRedacaoApp(App):
    status_message = "Cole o texto em outro app manualmente ou use Compartilhar Texto."

    def build(self):
        self.title = "Bot de Redação Android"
        return Builder.load_string(KV)

    def set_status(self, message: str):
        self.status_message = message
        if self.root:
            self.root.ids.status_label.text = message

    def open_url(self, url: str):
        webbrowser.open(url)
        self.set_status("Link aberto no navegador.")

    def copy_text(self, text: str):
        if not text.strip():
            self.set_status("Digite uma redação antes de copiar.")
            return
        Clipboard.copy(text)
        self.set_status("Texto copiado para a área de transferência.")

    def share_text(self, text: str):
        if not text.strip():
            self.set_status("Digite uma redação antes de compartilhar.")
            return

        if platform != "android":
            self.set_status("Compartilhamento Android só funciona no celular.")
            return

        from jnius import autoclass

        Intent = autoclass("android.content.Intent")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        String = autoclass("java.lang.String")

        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)
        intent.putExtra(Intent.EXTRA_TEXT, String(text))
        intent.setType("text/plain")

        current_activity = PythonActivity.mActivity
        chooser = Intent.createChooser(intent, String("Compartilhar redação via"))
        current_activity.startActivity(chooser)
        self.set_status("Escolha o app para colar/enviar a redação.")


if __name__ == "__main__":
    AndroidRedacaoApp().run()

from textwrap import wrap
import shutil

def important_message(text: str) -> str:

    terminal = shutil.get_terminal_size()[0]-50

    text = wrap(text, width = (terminal - 7))


    st = f"#{'=' * (terminal - 3)}#\n#{' ' * (terminal - 3)}#"
    txt = [f"#  {text[i].center(terminal - 7)}  #" for i in range(len(text))]
    end = f"#{' ' * (terminal - 3)}#\n#{'=' * (terminal - 3)}#"
    
    return f"{st}\n{'\n'.join(txt)}\n{end}"
 
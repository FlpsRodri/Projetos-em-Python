import pyautogui as pt

pt.alert("enviado para a impressora")
novamente = pt.alert("segundo")
pt.alert(text="Enviado para a impressora", title="Aviso",button=ok, timeout=none, root=novamente)
pt.alert()
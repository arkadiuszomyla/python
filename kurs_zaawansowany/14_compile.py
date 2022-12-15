
source = 'reportLine += 1'

reportLine = 0
exec(source)

# uruchamianie kodu skompilowanego jest szybsze
sourceCompiled = compile(source, 'internal variable source', 'exec')  #co skompilować, plik(skąd przeczytany), tryb
print(sourceCompiled)  # <code object <module> at 0x0000020BC1D53AA0, file "internal variable source", line 1>
exec(sourceCompiled)

print(reportLine)
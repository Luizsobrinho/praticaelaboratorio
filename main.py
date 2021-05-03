from conta import Conta
from cliente import Cliente

cli = Cliente('José Luiz','79996854830')
p1 = Conta(3432,0,cli)
p1.depositar(5000.00)


p1.listarExtrato()
p1.sacar(7000)
p1.sacar(85000)
p1.sacar(6000)

p1.listarExtrato()
from Populacao import Populacao
from Rainhas import Rainhas

if __name__ == "__main__":
  populacao = Populacao(Rainhas, 20)
  
  populacao.evoluir(30)
  
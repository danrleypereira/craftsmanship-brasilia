using System;

namespace TicTacToe
{
    public class Game
    {
        public string[,] tabuleiro = new string[3, 3];
        private const string playerOne = "X";
        private const string playerTwo = "O";
        private string quemEOProximoJogador = "X";
        private int numeroDaRodada = 1;
        public bool temUmVencedor = false;
        public string quemEOVencedor = "";

        public void jogar(int linha, int coluna)
        {
            if (numeroDaRodada % 2 == 0)
            {
                this.tabuleiro[linha, coluna] = this.quemEOProximoJogador;
                this.quemEOProximoJogador = "X";
                this.numeroDaRodada += 1;
            }
            else
            {
                this.tabuleiro[linha, coluna] = this.quemEOProximoJogador;
                this.quemEOProximoJogador = "O";
                this.numeroDaRodada += 1;
            }
        }
        public void verificarLinhas(){
            for(int index = 0; index < 3; index++)
            {
                if(
                    tabuleiro[index,0] != null && 
                    tabuleiro[index,0] == tabuleiro[index,1] 
                    && tabuleiro[index,0] == tabuleiro[index,2]
                )
                {
                    this.quemEOVencedor = tabuleiro[0,0];
                    this.temUmVencedor = true;
                    break;
                }
            }    
        }

        public void verificarColunas(){
            for(int index = 0; index < 3; index++)
            {
                if(
                    tabuleiro[0, index] != null && 
                    tabuleiro[0, index] == tabuleiro[1, index]
                    && tabuleiro[0, index] == tabuleiro[2, index]
                )
                {
                    this.quemEOVencedor = tabuleiro[0,0];
                    this.temUmVencedor = true;
                    break;
                }
            }    
        }
    }
}
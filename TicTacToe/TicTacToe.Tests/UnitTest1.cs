namespace TicTacToe.Tests;

public class UnitTest1
{
    [Fact]
    public void verificaSeXExisteNaPosicaoDada()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0);

        // Assert
        Assert.Equal("X", jogo.tabuleiro[0, 0]);
    }

    [Fact]
    public void verificaSeOExisteNaPosicaoDada()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0); //Jogada X
        jogo.jogar(0, 2); // Jogada O

        // Assert
        Assert.Equal("O", jogo.tabuleiro[0, 2]);
    }

    [Fact]
    public void verificaSeTerceiraJogadaE()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0); //Jogada X
        jogo.jogar(0, 2); // Jogada O
        jogo.jogar(1, 1); // Jogada X

        // Assert
        Assert.Equal("X", jogo.tabuleiro[1, 1]);
    }

    [Fact]
    public void verificaSeQuartaJogadaE()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0); //Jogada X
        jogo.jogar(0, 2); // Jogada O
        jogo.jogar(1, 1); // Jogada X
        jogo.jogar(0, 1); // Jogada O

        // Assert
        Assert.Equal("O", jogo.tabuleiro[0, 1]);
    }

    [Fact]
    public void verificaSeVencedorPrimeiraLinha()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0); //Jogada X
        jogo.jogar(1, 2); // Jogada O
        jogo.jogar(0, 1); // Jogada X
        jogo.jogar(1, 1); // Jogada O
        jogo.jogar(0, 2); // Jogada X
        jogo.verificarLinhas();

        // Assert
        Assert.True(jogo.temUmVencedor);
    }

    [Fact]
    public void verificaSeVencedorTerceiraLinha()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(2, 0); //Jogada X
        jogo.jogar(1, 2); // Jogada O
        jogo.jogar(2, 1); // Jogada X
        jogo.jogar(1, 1); // Jogada O
        jogo.jogar(2, 2); // Jogada X
        jogo.verificarLinhas();

        // Assert
        Assert.True(jogo.temUmVencedor);
    }

    [Fact]
    public void verificaSeVencedorTerceiraColuna()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0); //Jogada X
        jogo.jogar(1, 1); // Jogada O
        jogo.jogar(0, 1); // Jogada X
        jogo.jogar(1, 1); // Jogada O
        jogo.jogar(0, 2); // Jogada X
        jogo.verificarLinhas();

        // Assert
        Assert.True(jogo.temUmVencedor);
    }

    [Fact]
    public void verificaSeVencedorPrimeiraColuna()
    {
        // Arrange
        var jogo = new Game();

        //  Act
        jogo.jogar(0, 0); //Jogada X
        jogo.jogar(1, 1); // Jogada O
        jogo.jogar(0, 1); // Jogada X
        jogo.jogar(1, 1); // Jogada O
        jogo.jogar(0, 2); // Jogada X
        jogo.verificarLinhas();

        // Assert
        Assert.True(jogo.temUmVencedor);
    }
}
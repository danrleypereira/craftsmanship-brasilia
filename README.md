# Craftsmanship Brasília

Bem-vindo ao repositório do Craftsmanship Brasília! Este espaço é dedicado ao compartilhamento e à colaboração das soluções de katas desenvolvidas pelos membros de nossa comunidade. As atividades são realizadas tanto em nossos encontros presenciais quanto em sessões remotas síncronas, promovendo a prática contínua e o aperfeiçoamento das habilidades de programação em um ambiente amigável e de apoio mútuo.

## 🚀 Como Contribuir

Para contribuir com suas soluções de katas, siga os passos abaixo:

1. Clone este repositório.
2. Adicione sua solução na pasta correspondente ao kata que você resolveu. Caso não exista, sinta-se à vontade para criá-la.
3. Nomeie seus arquivos de forma clara e consistente, incluindo o nome do kata e a data, se possível.
4. Faça um pull request com suas alterações, seguindo as boas práticas de contribuição.

## 📚 Fontes de Katas

Nossas atividades são baseadas em katas retirados das seguintes fontes confiáveis. Você pode explorá-las para encontrar desafios que correspondam ao seu nível de habilidade ou áreas de interesse:

- [Kata Log](https://kata-log.rocks/)
- [Codurance Katas](https://www.codurance.com/katas)

## 📖 Princípios a Seguir

Ao resolver katas e contribuir para este repositório, incentivamos a aderência aos seguintes princípios fundamentais de desenvolvimento de software:

- **YAGNI (You Ain't Gonna Need It)**: Evite adicionar funcionalidades antes que elas sejam realmente necessárias.
- **KISS (Keep It Simple, Stupid)**: Prefira soluções simples e evite complexidade desnecessária.
- **DRY (Don't Repeat Yourself)**: Elimine redundâncias no código para melhorar a manutenção e a clareza.
- **Ciclo Red, Green, Refactor**: Siga este ciclo durante o TDD (Test-Driven Development) - comece escrevendo um teste que falha (Red), escreva o código mínimo necessário para passar no teste (Green) e, em seguida, refine e otimize o código sem alterar seu comportamento (Refactor).
- **Princípios SOLID**:
  - *Single Responsibility Principle*: Uma classe ou módulo deve ter apenas uma razão para mudar, focando em uma única responsabilidade.
  - *Open/Closed Principle*: As entidades de software devem estar abertas para extensão, mas fechadas para modificação direta.
  - *Liskov Substitution Principle*: Objetos de uma programa devem ser substituíveis por instâncias de seus subtipos sem alterar o funcionamento correto do programa.
  - *Interface Segregation Principle*: É melhor ter muitas interfaces específicas do que uma única interface geral.
  - *Dependency Inversion Principle*: Módulos de alto nível não devem depender de módulos de baixo nível, mas ambos devem depender de abstrações.
- **Clean Code**:
  - Escreva código claro e compreensível, com nomes significativos para variáveis, métodos e classes.
  - Mantenha funções e métodos focados em uma única ação ou propósito.
  - Utilize comentários de forma judiciosa para explicar "o porquê" por trás de um bloco de código, especialmente quando o código não é suficientemente autoexplicativo.

## 📝 Diretrizes para Estruturar e Nomear Testes

Ao escrever testes, é importante não apenas estruturá-los de forma clara, mas também nomeá-los de modo que descrevam o comportamento sendo testado. Duas metodologias populares para isso são **AAA (Arrange, Act, Assert)** para estruturar testes e **Given-Should-Then** para nomear e descrever testes.

### Estruturando Testes com AAA (Arrange, Act, Assert)

O padrão AAA é uma forma poderosa de organizar seus testes de forma que cada teste seja claro e conciso. Cada "A" representa uma seção do teste:

- **Arrange**: Preparação e configuração do ambiente de teste. Aqui você inicializa objetos, configura dados de entrada, e prepara o cenário para a ação que será testada.
- **Act**: A execução da funcionalidade que está sendo testada. Esta é a parte onde você invoca o método ou ação em questão.
- **Assert**: A verificação dos resultados obtidos. Aqui você vai afirmar se o resultado da ação está de acordo com o esperado.

**Exemplo de estruturação com AAA**:

```python
def test_calcula_idade_quando_data_de_nascimento_fornecida():
    # Arrange
    data_nascimento = date(2000, 1, 1)
    hoje = date(2022, 1, 1)
    
    # Act
    idade = calcular_idade(data_nascimento, hoje)
    
    # Assert
    assert idade == 22
```

### Nomeando Testes com Given-Should-Then

Given-Should-Then é uma convenção para nomear testes que descreve o cenário sendo testado, o comportamento esperado e o resultado esperado. Isso ajuda a tornar os nomes dos testes descritivos e a entender o propósito do teste à primeira vista.

- **Given**: Descreve o estado inicial ou as condições prévias antes da execução do teste.
- **Should**: Explica o comportamento ou a ação que está sendo testada.
- **Then**: Descreve o resultado esperado ou o estado final após a execução do teste.

**Exemplos de nomes de testes com Given-Should-Then**:

- `GivenContaBancariaComSaldo100_WhenSacar50_ThenSaldoDeveSer50`
- `GivenUsuarioMenorDeIdade_WhenTentarCriarConta_ThenDeveRetornarErroDeIdadeMinima`

### Organizando Testes

Ao organizar seus testes, agrupe-os de forma lógica, seja por funcionalidade, por cenário de uso ou outro critério que faça sentido para o seu projeto. Dentro de cada grupo, aplique as estratégias de estruturação e nomenclatura de testes para garantir que cada teste seja autoexplicativo e fácil de entender. Comentar o propósito de cada grupo de testes ou testes individuais também pode ajudar outros desenvolvedores a navegar e entender o conjunto de testes mais rapidamente.

Lembre-se, a clareza e a manutenibilidade dos testes são tão importantes quanto a do código de produção. Testes bem escritos e organizados são fundamentais para a saúde a longo prazo do seu projeto.

## 🤝 Contribuindo

Agradecemos sua contribuição para enriquecer este repositório e a comunidade. Se tiver sugestões, dúvidas ou desejar colaborar de outra forma, sinta-se à vontade para abrir uma issue ou entrar em contato conosco.
const form = document.getElementById('formulario');

const tabela = document.getElementById('corpo-tabela');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = form.nome.value;
    const matricula = form.matricula.value;
    const nota1 = parseFloat(form.nota1.value);
    const nota2 = parseFloat(form.nota2.value);
    const media = (nota1 + nota2) / 2;
    const situacao = (media >= 5) ? 'Aprovado' : 'Reprovado';

    const newRow = tabela.insertRow();

    newRow.innerHTML = `
        <td>${nome}</td>
        <td>${matricula}</td>
        <td>${nota1}</td>
        <td>${nota2}</td>
        <td>${media.toFixed(1)}</td>
        <td>${situacao}</td>
    `;

    form.reset();
});
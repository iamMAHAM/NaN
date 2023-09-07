function snake_case(chaine) {
  if (typeof chaine === 'string') {
    const miniscules = 'abcdefghijklmnopqrstuvwxyz';
    const majuscules = miniscules.toUpperCase();
    let resultat = '';

    for (const caractere of chaine) {
      if (!(miniscules + majuscules).includes(caractere)) {
        return "la chaine n'est pas en camelcase";
      }

      const indice = chaine.indexOf(caractere);

      if (indice === 0) {
        if (majuscules.includes(caractere)) {
          return "la chaine n'est pas en camelcase";
        }
        resultat += caractere;
      } else {
        if (majuscules.includes(caractere)) {
          resultat += `_${caractere.toLowerCase()}`;
        } else {
          resultat += caractere;
        }
      }
    }

    return resultat;
  }

  return "la chaine n'est pas en camelcase";
}

tests = [
  'salutLaTeam',
  'salut_la_team',
  'salut_la_Team',
  'SalutLaTeam',
  'salutlateam',
  'salut la team',
  'salut_lateam',
  'salut_la_team_',
  '_salut_la_team',
  'salut_la_team_',
  'salut__la_team',
  'salut_la__team',
  'salut_la_team_',
  'salut_la_team_',
  'salut_la_team_',
];

for (const test of tests) {
  console.log(snake_case(test));
}

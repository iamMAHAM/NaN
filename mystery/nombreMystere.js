function generateNumber() {
    return Math.floor(Math.random() * 100);
  }
  
  function nombreMystere() {
    const generee = generateNumber();
    let nombreTentative = 5;
    let naPasTrouve = true;
  
    do {
      let entree = parseInt(prompt('Entrez un nombre compris entre 0 et 100'));
  
      if (entree === generee) {
        alert(`Mes félicitations vous avez trouvé la bonne reponse : ${generee}`);
        naPasTrouve = false;
      } else {
        nombreTentative -= 1;
        if (entree > generee) {
          alert("C'est moins ");
        } else {
          alert("C'est plus");
        }
      }
  
      if (nombreTentative === 0) {
        alert('Vous avez perdu ');
        naPasTrouve = false;
      }
    } while (naPasTrouve);
  
    //   while (entree !== generee) {
    //     if (nombreTentative === 0) {
    //       alert('Vous avez perdu ');
    //       break;
    //     }
    //     if (entree > generee) {
    //       alert("C'est moins ");
    //     } else if (entree < generee) {
    //       alert("C'est plus");
    //     } else {
    //       alert(`Mes félicitations vous avez trouvé la bonne reponse : ${generee}`);
    //       break;
    //     }
    //     nombreTentative -= 1;
    //     entree = parseInt(prompt('Entrez un nombre compris entre 0 et 100'));
    //   }
  }
  nombreMystere();
  
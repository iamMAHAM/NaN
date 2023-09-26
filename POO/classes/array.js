class Tableau {
  constructor(...props) {
    this.tableau = [...props];
  }

  get length() {
    let compteur = 0;
    while (this.tableau[compteur] !== undefined) {
      compteur++;
    }
    return compteur;
  }

  /**
   *
   * @param {number} indice
   */
  at(indice) {
    if (indice < 0) {
      indice = this.length + indice;
    }
    return this.tableau[indice];
  }

  concat(...tabs) {
    console.log(tabs);
    const concatene = new Tableau();
    for (const tab of tabs) {
      if (!tab instanceof Tableau) {
        throw new TypeError(
          `Le paramètre ${tab} n'est pas une instance de Tableau`
        );
      }
    }
  }
}

tab = new Tableau('s', 'a', 'b', 'c');
// tab2 = new Tableau(1, 2, 3);
tab.concat(new Tableau(1, 2), new Tableau(3, 4), new Tableau(5, 6), 5);

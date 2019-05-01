export class Beers {

  constructor(
    public id: number,
    public beer_name: string,
    public description: string,
    public harmonization: string,
    public color: string,
    public alcohol: string,
    public temperature: string,
    public ingredients: object
  ){ }
}

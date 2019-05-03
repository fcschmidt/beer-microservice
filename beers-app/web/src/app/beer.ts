/*export interface Beer {
    id: number,
    beer_name: string,
    description: string,
    color: string,
    alcohol: string,
    temperature: string,
    harmonization: string,
    ingredients: []
}*/

export class Beer {
  id: number;
  beer_name: string;
  description: string;
  color: string;
  alcohol: string;
  temperature: string;
  harmonization: string;
  ingredients: [{names: [string]}]
}

export class BeerUpdate {
  id: number;
  beer_name: string;
  description: string;
  color: string;
  alcohol: string;
  temperature: string;
  harmonization: string;
  ingredients: {
    list: [
      {
        ingredient_name: string,
        id: number,
        beer_id: number
      }];
  };
}


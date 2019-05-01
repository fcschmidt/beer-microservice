import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from "@angular/common/http";
import { Observable } from "rxjs";
// import { map } from "rxjs/operators";

import { Ingredient } from "./ingredient";

@Injectable({
  providedIn: 'root'
})
export class IngredientService {

  private API_URL = 'http://localhost:5000/api/v1/ingredients';

  constructor(private http: HttpClient) { }

  /*POST: Add a new ingredient to the server. */
  /*createIngredient(ingredient): Observable<Ingredient>{
    const url = `${this.API_URL}`
  }*/

  /*DELETE: Delete the ingredient from the server. */
  deleteIngredient(ingredient): Observable<Ingredient>{
    const url = `${this.API_URL}/${ingredient.id}`;
    return this.http.delete<Ingredient>(url);
  }
}

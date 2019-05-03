import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
// import { map } from "rxjs/operators";
// import { catchError, tap } from "rxjs/operators";

import { Ingredient } from "./ingredient";



@Injectable({
  providedIn: 'root'
})
export class IngredientService {

  private apiUrl = 'http://localhost:5000/api/v1/ingredients';

  httpOptions = {
    headers:new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) { }


  /*POST: Add a new ingredient to the server. */
  addIngredient(ingredient): Observable<Ingredient> {
    return this.http.post<Ingredient>(this.apiUrl, ingredient, this.httpOptions);
  }

  /*DELETE: Delete the ingredient from the server. */
  deleteIngredient(ingredient): Observable<Ingredient>{
    const url = `${this.apiUrl}/${ingredient.id}`;
    return this.http.delete<Ingredient>(url);
  }



}

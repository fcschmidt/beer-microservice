import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";

import { Beer } from './beer'

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class BeerService {

  private apiUrl = 'http://localhost:5000/api/v1/beers';

  constructor(private http: HttpClient) { }

  public getBeers(): Observable<Beer[]>{
    return this.http.get<Beer[]>(this.apiUrl)
  }

  public getBeer(beerId: number): Observable<Beer>{
    const url =`${this.apiUrl}/${beerId}`;
    return this.http.get<Beer>(url)
  }

  // Methods

  /* POST: Add a new beer to the server */


  /* PUT: Update the beer on the server */


  /* DELETE: Delete the beer from the server */

}

import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import { Observable } from "rxjs";
import { map } from "rxjs/operators";


import { Beer } from './beer'


@Injectable({
  providedIn: 'root'
})
export class BeerService {

  private API_URL = 'http://localhost:5000/api/v1/beers';

  constructor(private http: HttpClient) { }

  /* GET: beers from the server. */
  getBeers(): Observable<Beer[]>{
    return this.http.get<Beer[]>(this.API_URL)
  }

  /* GET: beer by id. */
  getBeer(beerId: number): Observable<Beer>{
    const url =`${this.API_URL}/${beerId}`;
    return this.http.get<Beer>(url)
  }

  // Methods

  /* POST: Add a new beer to the server. */
  createBeer(parans) {
    let headers = new HttpHeaders({'Content-Type': 'application/x-www-form-urlencoded'});

    return this.http.post(this.API_URL, parans)

  }
  /* PUT: Update the beer on the server. */


  /* DELETE: Delete the beer from the server. */
  deleteBeer(beer): Observable<Beer>{
    const url = `${this.API_URL}/${beer.id}`;
    return this.http.delete<Beer>(url);
  }
}

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import { Observable, throwError} from "rxjs";
// import { catchError, map, retry} from "rxjs/operators";


import { Beer } from './beer'


@Injectable({
  providedIn: 'root'
})
export class BeerService {

  private apiUrl = 'http://localhost:5000/api/v1/beers';

  httpOptions = {
    headers:new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) { }

  /*
  *  Methods for consuming RESTful API
  * */

  /* GET: beers from the server. */
  getBeers(): Observable<Beer[]>{
    return this.http.get<Beer[]>(this.apiUrl)
  }

  /* GET: beer by id. */
  getBeer(beerId: number): Observable<Beer>{
    const url =`${this.apiUrl}/${beerId}`;
    return this.http.get<Beer>(url)
  }

  /* POST: Add a new beer to the server. */
  addBeer(beer): Observable<Beer> {
    return this.http.post<Beer>(this.apiUrl, beer, this.httpOptions)
    /*return this.http.post<BeerAdd>(this.API_URL, newBeer, {
      headers: {
        'Content-Type': 'application/json'
      }
    });*/
  }
  /* PUT: Update the beer on the server. */
  /*updateBeer(editedBeer: Beer): Observable<Beer> {
    const url = `${this.API_URL}/${id}`;
    // return this.http.post<Beer>(url, JSON.stringify(beer), this.httpOptions)
    return this.http.post<Beer>(url, editedBeer, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }*/

  /* DELETE: Delete the beer from the server. */
  deleteBeer(beer): Observable<Beer>{
    const url = `${this.apiUrl}/${beer.id}`;
    return this.http.delete<Beer>(url);
  }

  // Error handling
  /*handleError(error){
    let errorMessage="";
    if(error.error instanceof ErrorEvent){
    //  Get client-side error
      errorMessage = error.error.nessage;
    } else {
    //  Get server-side error
      errorMessage = `Error Code: ${error.status}\nMessage:${error.message}`;
    }
    window.alert(errorMessage);
    return throwError(errorMessage);
  }*/
}

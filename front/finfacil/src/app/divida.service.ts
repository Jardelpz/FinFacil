import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { DividaModel } from './dividas/dividas.model';

@Injectable({
  providedIn: 'root'
})

export class DividaService {

  constructor(private http: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  postDivida(divida: DividaModel, email: string) : Observable<any>{
    return this.http.post('http://localhost:5000/divida?email='+email, divida)
  }

  listDividas(email: string): Observable<any>{
    return this.http.get('http://localhost:5000/divida?email='+email) 
  }

  pagarDivida(id: number): Observable<any>{
    let url = 'http://localhost:5000/divida/pagar?id='+id
    console.log(url)
    let any= {
      "is_pago":"D"
    }
    return this.http.get(url)
  }

  somaDivida(email:string){
    return this.http.get('http://localhost:5000/divida/soma?email='+email)
  }

}

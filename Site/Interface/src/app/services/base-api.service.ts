import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs'; 

@Injectable({
  providedIn: 'root'
})
export class BaseApiService {

  private baseUrl = "http://localhost:3000"//конечная точка url

  constructor(public http: HttpClient) {

  }
  /*GET — метод для чтения данных с сайта. 
  Например, для доступа к указанной странице.
  Он говорит серверу, что клиент хочет прочитать указанный документ. */
  

  //получаем адрес, откуда данные будут подгружаться
  private getUrl(url: string = ""): string/* eto тип возвращаемого значения*/ {
       return this.baseUrl + url; //url по которому получим данные
  }

  public get(url: string = "", header: HttpHeaders): Observable<any> {
    let requestOptions = {
      headers: header
    };
    return this.http.get(this.getUrl(url), requestOptions);
  }
}

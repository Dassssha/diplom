import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BaseApiService {

  private baseUrl = "http://localhost:3000"

  constructor(public http: HttpClient) {

  }

  private getUrl(url: string = ""): string {
    return this.baseUrl + url;
  }

  public get(url: string = "", header: HttpHeaders): Observable<any> {
    let requestOptions = {
      headers: header
    };
    return this.http.get(this.getUrl(url), requestOptions);
  }
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GostsService {
  constructor(private http: HttpClient) {
  }

  getAllGosts(): Promise<any> {
    return this.http.get(environment.baseUrl + '').toPromise();
  }

  getGostParams(gost: string, type: string): Promise<any> {
    return this.http.get(`${environment.baseUrl}/${gost}/${type}`).toPromise();
  }

  createGost(gost: string, type: string): Promise<any> {
    return this.http.post(`${environment.baseUrl}/test`, {
      gosts: gost,
      types: type,
    }).toPromise();
  }
}

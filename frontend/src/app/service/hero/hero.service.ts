import { Injectable } from '@angular/core';
import { Observable, of} from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import {MessageService} from '../message/message.service';

import { Hero } from'../../models/Hero';
import { HEROES } from '../../models/mock-heroes';

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  private urlList = 'http://localhost:5000/api/heroes';

  constructor(
    private http: HttpClient,
    private messageService: MessageService
    ) { }

  /**
   * List
   */
  getHeroes(): Observable<Hero[]> {
    this.messageService.add('HeroService: fetch heroes');
  
    return this.http.get<Hero[]>(this.urlList)
      .pipe(
        tap(_ => this.log('fetched heroes')),
        catchError(this.handleError('getHeroesError', []))
      )
    // return of(HEROES);
  }

  /**
   * Get by id
   * @param id hero id 
   */
  getHero(id: number): Observable<Hero> {
    this.messageService.add('Get hero by id');
    return of(HEROES.find(hero => hero.id === id));
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
       console.error(error); 
       this.log(`${operation} failed: ${error.message}`);
       return of(result as T);
    };
  }
 
  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }
}

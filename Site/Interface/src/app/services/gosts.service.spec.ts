import { TestBed } from '@angular/core/testing';

import { GostsService } from './gosts.service';

describe('GostsService', () => {
  let service: GostsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GostsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

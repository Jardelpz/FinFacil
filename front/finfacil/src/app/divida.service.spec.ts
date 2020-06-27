import { TestBed } from '@angular/core/testing';

import { DividaService } from './divida.service';

describe('DividaService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DividaService = TestBed.get(DividaService);
    expect(service).toBeTruthy();
  });
});

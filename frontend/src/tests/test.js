import { renderHook, act } from '@testing-library/react-hooks';
import article from './article';
test('useCounter increments and decrements count', () => {
    const { result } = renderHook(() => article());

  });
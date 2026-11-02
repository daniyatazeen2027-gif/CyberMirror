import { API_ENDPOINTS } from '../constants/apiEndpoints';

export async function getAlerts() {
  const response = await fetch(API_ENDPOINTS.ALERTS);

  if (!response.ok) {
    throw new Error(`Unable to fetch alerts (HTTP ${response.status})`);
  }

  return response.json();
}

# Install and import a Kalman filter package
!pip install pykalman
from pykalman import KalmanFilter

# Fetch some minute bar data
symbol = ['FRC']
start_time = pd.to_datetime("2023-03-13 09:30").tz_localize('America/New_York')
end_time = pd.to_datetime("2023-03-13 16:00").tz_localize('America/New_York')

min_bars = api_data.get_bars(symbol,
                         '1Min',
                         start=start_time.isoformat(),
                         end=end_time.isoformat(),
                         ).df

# Instantiate a Kalman filter and use it to smooth the minute data
kf = KalmanFilter(transition_matrices = [1],
                  observation_matrices = [1],
                  initial_state_mean = 0,
                  initial_state_covariance = 1,
                  observation_covariance=1,
                  transition_covariance=.01)

smoothed_data, _ = kf.filter(min_bars.close)